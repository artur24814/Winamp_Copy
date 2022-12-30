'''
Helper functions
'''


#convert int number to time format
def convert_duration_to_show(duration):
    duration_to_show = (duration / 1000) / 60
    duration_list = str(format(duration_to_show, '.2f')).split('.')
    return duration_list

#get Html template
def get_html(time):
    return '''
    <!DOCTYPE HTML>
    <html>
    <body>
    <table border="0" style="width: 100vw;">
    <thead>
    <tr>
    <td align="left">
    <span style="font-family:'Monaco'; font-weight:600;">▶</span></td>
    <td align="right">
    <span style=" font-family:'Fantasy'; font-size:28px; font-weight:600;">&nbsp;&nbsp;&nbsp;&nbsp;0%s</span>
    </td>
    </tr>
    </thead>
    </table>
    </body>
    </html>
    ''' % time

