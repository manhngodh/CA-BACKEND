from app import create_app  # Import the create_app function
import os 

# Create the Flask app instance using the create_app function
app = create_app()

# Register blueprints
# app.register_blueprint(student_blueprint, url_prefix='/students')
# app.register_blueprint(volunteer_blueprint, url_prefix='/volunteers')

@app.route('/test')
def test():
    return 'test created'
if __name__ == '__main__':
    print('Manh', os.environ.get('DATABASE_URL'))
    app.run(host='0.0.0.0', port=5000) 