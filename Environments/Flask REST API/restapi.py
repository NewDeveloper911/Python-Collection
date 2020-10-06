from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
#this is used to set up the location of my database
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    '''
    This creates a field name id, which is of type integer, and sets it as the
    primary key, which is the unique number set to each record in my
    database
    '''
    name = db.Column(db.String(100), nullable=False)
    '''
    Nullable means that a piece of data can not have any data in it.
    That's not what we want
    '''
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name={name}, views = {views}, likes = {likes})"

#db.create_all() #this was used to create my database the first time only

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)
video_put_args.add_argument("views", type=int, help="Total views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Total likes of the video", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video", required=False)
video_update_args.add_argument("views", type=int, help="Total views of the video", required=False)
video_update_args.add_argument("likes", type=int, help="Total likes of the video", required=False)

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

##def abort_if_not(video_id):
##    if video_id not in videos:
##        abort(404, message="Video doesn't exist, couldn't find video")
##        '''
##        404 is an error status code for when we cannot find something,
##        usually because it doesn't exist. abort() will take in that error code
##        and then end the current process
##        '''
##
##def abort_if_exist(video_id):
##    if video_id in videos:
##        abort(409, message="Video already exists")
##        '''
##        409 is an error status code for when we cannot create a new object
##        because it already exists
##        '''


class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        #represent get method
        #abort_if_not(video_id)
        result = VideoModel.query.filter_by(id=video_id).first()
        '''
        This will filter through all of my videos to see if any match
        with the id i'm looking for and select the first video which matches
        (should be the one with the lowest id/index)
        '''
        if not result:
            abort(404, message="Coudln't find video with the specified id")
        return result
    '''
    The @marshal_with decorator, along with the resource_fields are used to
    serialise my database into a JSON format, which can be easily formatted
    and outputted as suitable strings, instead of creating an instance of the
    database
    '''
    @marshal_with(resource_fields)
    def put(self, video_id):
        #represent put method
        #abort_if_exist(video_id)
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video id taken")
##        videos[video_id] = args
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        #I am fetching arguments from args and inputting them into
        #an instance of VideoModel
        db.session.add(video) #like git add, temporarily adds changes
        db.session.commit() #like git commit, permanently adds changes
        return video, 201
        # code says that this has been created successfully

    @marshal_with(resource_fields)
    def patch(self, video_id):
        #represents patch method
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video doesn't exist, cannot update non-existent things")
        if args['name']:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']
            #ineffienct way to replace and update variables
            
        db.session.commit()

        return result
    
    def delete(self, video_id):
        #represents delete method
        #abort_if_not(video_id)
        del videos[video_id]
        return '', 204
        #status code 209 means something has been deleted successfully
    
api.add_resource(Video, "/video/<int:video_id>")
# This ays that it wants an int named video_id and process that info

if __name__ == "__main__":
    app.run(debug=True)
