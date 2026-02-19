from youtrack.connection import Connection

def get_student_tickets(youtrack_url, token, project_id):
    yt = Connection(youtrack_url, token)
    tickets = yt.get_issues(project_id, "State: Open", limit=100)
    
    student_bugs = []
    for ticket in tickets:
        student_bugs.append({
            'id': ticket['id'],
            'title': ticket['summary'],
            'description': ticket['description'],
            'student': ticket['reporterName']
        })
    return student_bugs
