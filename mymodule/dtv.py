"""
view a pandas dataframe in a datatable
"""
from tempfile import NamedTemporaryFile
import webbrowser

BASE_HTML = """
<!doctype html>
<html><head>
<meta http-equiv="Content-type" content="text/html; charset=utf-8">
<script type="text/javascript"
src="https://code.jquery.com/jquery-3.3.1.js"></script>
<script type="text/javascript"
src="https://cdn.datatables.net/1.10.20/js/jquery.dataTables.min.js"></script>
<script type="text/javascript"
src="https://cdn.datatables.net/buttons/1.6.1/js/dataTables.buttons.min.js"></script>
<script type="text/javascript"
src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js"></script>
<script type="text/javascript"
src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/pdfmake.min.js"></script>
<script type="text/javascript"
src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/vfs_fonts.js"></script>
<script type="text/javascript"
src="https://cdn.datatables.net/buttons/1.6.1/js/buttons.html5.min.js"></script>
<link rel="stylesheet" type="text/css"
href="https://cdn.datatables.net/1.10.20/css/jquery.dataTables.css">
</head><body>%s<script type="text/javascript">$(document).ready(function()
{var table = $('table').DataTable({
    pageLength: 50,
    lengthMenu: [ [100, 250, 1000, -1], [100, 250, 1000, "All"]],
    autoWidth: true,
    dom: 'lfrtBip',
    buttons: [ 'copyHtml5', 'excelHtml5', 'csvHtml5' ]
});});</script>
</body></html>
"""

def df_html(df):
    """
    :parma df: pandas dataframe
    convert pandas dataframe to HTML table
    classes refer to datatable styling
    """
    df_html = df.to_html(border=0,
            classes="cell-border compact hover order-column row-border stripe")
    return BASE_HTML % df_html

def dtv(df):
    """
    View pandas dataframe in web browser
    :param df: pandas dataframe
    """
    with NamedTemporaryFile(delete=False, mode='w+', suffix='.html') as f:
        f.write(df_html(df))
    webbrowser.open('file://' + f.name)
