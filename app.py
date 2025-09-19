from flask import Flask, render_template_string

app = Flask(__name__)

def Hello():
    """Генерирует красивую HTML страницу с приветствием от Илона Маска"""
    html_template = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Приветствие от Илона Маска</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                margin: 0;
                padding: 0;
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            
            .container {
                background: white;
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                text-align: center;
                max-width: 600px;
                margin: 20px;
            }
            
            .elon-image {
                width: 150px;
                height: 150px;
                border-radius: 50%;
                object-fit: cover;
                margin-bottom: 20px;
                border: 4px solid #667eea;
            }
            
            h1 {
                color: #333;
                margin-bottom: 20px;
                font-size: 2.5em;
            }
            
            .message {
                color: #666;
                font-size: 1.2em;
                line-height: 1.6;
                margin-bottom: 30px;
            }
            
            .signature {
                font-style: italic;
                color: #888;
                font-size: 1.1em;
                margin-top: 30px;
            }
            
            .cucumber {
                font-size: 3em;
                margin: 20px 0;
                animation: bounce 2s infinite;
            }
            
            @keyframes bounce {
                0%, 20%, 50%, 80%, 100% {transform: translateY(0);}
                40% {transform: translateY(-30px);}
                60% {transform: translateY(-15px);}
            }
            
            .highlight {
                color: #4CAF50;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Добро пожаловать в будущее! 🚀</h1>
            
            <div class="message">
                <p>Приветствую вас, земляне!</p>
                <p>Сегодня особенный день - мы празднуем <span class="highlight">День Огурца</span>!</p>
                
                <div class="cucumber">🥒</div>
                
                <p>Поздравляю всех с этим замечательным праздником! Помните, что даже самый маленький огурец может стать частью большого космического салата!</p>
                
                <p>Мечтайте о великом, как будто вы можете изменить мир... потому что так оно и есть!</p>
            </div>
            
            <div class="signature">
                С уважением и верой в будущее,<br>
                <strong>Илон Маск</strong><br>
                CEO SpaceX & Tesla
            </div>
        </div>
    </body>
    </html>
    """
    return html_template

@app.route('/')
def hello():
    return Hello()

@app.route('/health')
def health():
    return "ok", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)