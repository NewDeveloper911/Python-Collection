from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)
video_put_args.add_argument("views", type=int, help="Total views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Total likes of the video", required=True)

videos = {}

class Video(Resource):
    def get(self, video_id):
        #represent get method
        return videos[video_id]
    
    def put(self, video_id):
        #represent put method
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201 # code says that this has been creasted successfully
    
    
api.add_resource(Video, "/video/<int:video_id>")
# This ays that it wants an int named video_id and process that info

if __name__ == "__main__":
    app.run(debug=True)
