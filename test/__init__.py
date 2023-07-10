from flask import Flask

def create_app():
    app = Flask(__name__)

    # main_views 내부에 있는 bp를 통한 라우팅 함수들을 등록
    from views import main_views
    app.register_blueprint(main_views.bp)

    return app

