from kivy.utils import platform

if platform == 'android':

    from jnius import autoclass, cast
    from android.runnable import run_on_ui_thread

    context = autoclass('org.renpy.android.PythonActivity').mActivity
    Toast = autoclass('android.widget.Toast')
    String = autoclass('java.lang.String')
    Intent = autoclass('android.content.Intent') 

    def charseq(text):
        return cast('java.lang.CharSequence', String(text))


    @run_on_ui_thread
    def toast(text):

        text = charseq(text)
        mi_toast = Toast.makeText(context, text, Toast.LENGTH_SHORT)
        mi_toast.show()


    @run_on_ui_thread
    def share(text):

        text, subject = charseq(text), charseq(text.replace(' ', '-'))

        intent = Intent()
        intent.setAction(Intent.ACTION_SEND)

        intent.putExtra(Intent.EXTRA_SUBJECT, subject)
        intent.putExtra(Intent.EXTRA_TEXT, text)

        intent.setType('text/plain')

        context.startActivity(intent)

else:
    toast = print
    share = print
