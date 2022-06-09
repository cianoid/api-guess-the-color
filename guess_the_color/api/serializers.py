from rest_framework import serializers

from core.guess import GuessColor


class GuessSerializer(serializers.Serializer):
    number = serializers.IntegerField(
        required=True, min_value=1, max_value=100)

    def to_representation(self, instance):
        self.run_validation(data=instance)

        guess = GuessColor(instance.pop('number'))

        return {'color_name': guess.guess_the_color()}
