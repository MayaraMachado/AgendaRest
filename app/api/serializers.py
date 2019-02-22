from rest_framework import serializers
from app.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class AgendamentoSerializer(serializers.ModelSerializer):
    # criador = serializers.HyperlinkedRelatedField(many=False, view_name='profiles-details', read_only=True)
    # convidados = UserSerializer(many=True, partial=True)
    # criador = UserSerializer( partial=True)
    # convidados = serializers.HyperlinkedRelatedField(many=True, view_name='profiles-details', read_only=True)
    class Meta:
        model = Agendamento
        fields = ['criador', 'titulo', 'descricao', 'data', 'hora', 'local', 'convidados', 'publico']

    def create(self, validated_data, id=None):
        publico = validated_data['publico']
        
        criador = validated_data['criador']
        del validated_data['criador']
        user = User.objects.get(pk=criador.id)

        agenda = Agendamento.objects.create(criador=user, titulo=validated_data['titulo'], descricao=validated_data['descricao'], data=validated_data['data'], hora=validated_data['hora'], local=validated_data['local'], publico=validated_data['publico'])

        convidados = validated_data['convidados']
        if  publico and convidados:
            del validated_data['convidados']
            convidados = []
            
            
        for user in convidados:
            agenda.convidados.add(user)

        return agenda

