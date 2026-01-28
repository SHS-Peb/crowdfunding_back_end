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
    
    has_active_or_pending = Fundraiser.objects.filter(
      owner=request.user
    ).exclude(
      status="REJECTED"
    ).exists()

    if has_active_or_pending:
      raise serializers.ValidationError({"detail": "You already have a fundraiser pending or approved. You can only resubmit if it is rejected."})
    return attrs


class PledgeSerializer(serializers.ModelSerializer):
  class Meta:
     model = apps.get_model('fundraisers.Pledge')
     fields = '__all__'

class FundraiserDetailSerializer(FundraiserSerializer):
   pledges = PledgeSerializer(many=True, read_only=True)