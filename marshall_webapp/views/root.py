from pyramid.response import Response
from pyramid.view import view_config
import pessto_marshall_engine.webapp.marshall as wa


@view_config(route_name='home', renderer='marshall_webapp:templates/mytemplate.pt')
def my_view(request):
    rows = request.db.execute(
        "SELECT * FROM meta_workflow_lists_counts").fetchall()
    rows = str(rows)
    return {'project': rows}


# @view_config(name='hello', request_method='GET')
# def my_view(request):
#     return Response('Hello')
