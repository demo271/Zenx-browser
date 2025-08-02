def log_search(query, user):
    with open('logs/search_history.log', 'a') as f:
        f.write(f"{user} searched for: {query}\n")
