from flask_restful import Resource, reqparse
from app.tables import Character

postParser: reqparse.RequestParser = reqparse.RequestParser()

postParser.add_argument('id', type=int)
postParser.add_argument('name', type=str)
postParser.add_argument('rarity', type=int)
postParser.add_argument('name_en', type=str)
postParser.add_argument('full_name', type=str)
postParser.add_argument('card', type=str)
postParser.add_argument('weapon', type=str)
postParser.add_argument('eye', type=str)
postParser.add_argument('sex', type=str)
postParser.add_argument('birthday', type=int)
postParser.add_argument('region', type=str)
postParser.add_argument('affiliation', type=str)
postParser.add_argument('portrait', type=bytes)
postParser.add_argument('description', type=str)

deleteParser: reqparse.RequestParser = reqparse.RequestParser()

deleteParser.add_argument('id', type=int, required=True)

patchParser: reqparse.RequestParser = reqparse.RequestParser()

patchParser.add_argument('id', type=int, required=True)
patchParser.add_argument('name', type=str)
patchParser.add_argument('rarity', type=int)
patchParser.add_argument('name_en', type=str)
patchParser.add_argument('full_name', type=str)
patchParser.add_argument('card', type=str)
patchParser.add_argument('weapon', type=str)
patchParser.add_argument('eye', type=str)
patchParser.add_argument('sex', type=str)
patchParser.add_argument('birthday', type=int)
patchParser.add_argument('region', type=str)
patchParser.add_argument('affiliation', type=str)
patchParser.add_argument('portrait', type=bytes)
patchParser.add_argument('description', type=str)


class Characters(Resource):

    @staticmethod
    def get() -> (dict, int):
        characters: list = Character.query.filter()
        if characters is not None:
            return [item.as_dict() for item in characters], 200
        return {
                   'message': 'Не найдено ни одного персонажа.'
               }, 404

    @staticmethod
    def post() -> (dict, int):
        '''not work yet'''
        args: dict = postParser.parse_args()
        character = Character()
        Character.update(character.setValues(args))

        return {
                   'message': 'Success'
               }, 200

    @staticmethod
    def delete():
        args: dict = deleteParser.parse_args()

        character = Character.query.filter(Character.id == args['id']).first()

        try:
            Character.delete(character)
        except:
            return {
                       'message': 'id do not found'
                   }, 404
        return {
                   'message': 'Success'
               }, 200

    @staticmethod
    def patch():
        '''not work yet'''
        args: dict = patchParser.parse_args()

        character = Character.query.filter(Character.id == args['id']).first()
        character.setValues(args)

        return {
                   'message': 'success'
               }, 200