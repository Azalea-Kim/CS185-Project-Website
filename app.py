from flask import Flask, send_from_directory

app = Flask(
    __name__,
    static_folder="full/public",
    template_folder="full/public",
    static_url_path=""              # 关键：让 /css /js /images 直接生效
)
@app.route('/')
def index():
    return send_from_directory(app.template_folder, "index.html")

if __name__ == "__main__":
    app.run(debug=True)