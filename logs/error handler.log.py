@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error_message="Page not found."), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('error.html', error_message="Internal server error."), 500
