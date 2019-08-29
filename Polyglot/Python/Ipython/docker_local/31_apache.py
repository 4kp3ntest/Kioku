
class Apache():


    def __init__(self):

        self.client = client

    def start(self):

        try:
            apache = self.client.containers.get('apache')
            apache.kill()
            apache.remove()
        except:
            pass

        apache_cmnd = '{} {} apache'.format(dstr_apache, obelix)
        subprocess.call(apache_cmnd, shell=True)
        self.apache = self.client.containers.get('apache')


apache = Apache()