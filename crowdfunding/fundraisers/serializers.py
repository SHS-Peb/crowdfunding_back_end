from rest_framework import serializers
from django.apps import apps

Fundraiser = apps.get_model("fundraisers", "Fundraiser")

class FundraiserSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.id')
  
  class Meta:
      model = Fundraiser
      fields = '__all__'

  def validate(self, attrs):
    request = self.context.get("request")

    if request is None or request.user.is_anonymous:
        return attrs

    # Only admins can change status
    if "status" in attrs and not request.user.is_staff:
        raise serializers.ValidationError({
            "status": "Only administrators can change fundraiser status."
        })

    # One fundraiser at a time rule
    has_active_or_pending = Fundraiser.objects.filter(
        owner=request.user
    ).exclude(
        status="REJECTED"
    ).exists()

    if has_active_or_pending and self.instance is None:
        raise serializers.ValidationError({
            "detail": (
                "You already have a fundraiser pending or approved. "
                "You can only resubmit if it is rejected."
            )
        })

    return attrs



class PledgeSerializer(serializers.ModelSerializer):
  supporter = serializers.ReadOnlyField(source="supporter.id")
  
  class Meta:
     model = apps.get_model('fundraisers.Pledge')
     fields = '__all__'

  def validate(self, attrs):
    fundraiser = attrs.get("fundraiser")

    if fundraiser is None:
        return attrs

    if fundraiser.status != "APPROVED":
        raise serializers.ValidationError({
            "detail": "This fundraiser has not been approved yet."
        })

    if not fundraiser.is_open:
        raise serializers.ValidationError({
            "detail": "This fundraiser is closed for pledges."
        })

    return attrs

class FundraiserDetailSerializer(FundraiserSerializer):
   pledges = PledgeSerializer(many=True, read_only=True)