from Sample.graduateMessageSample.Task.GraduateMessageTask import GraduateMessageTask
from Task.TaskMessage import TaskMessage



if __name__ == '__main__':

    ss = ''
    ml = ''
    zy = '法学'
    file_path = './dic/'+ml+zy+'.csv'

    GraduateMessageTask(file_path,ss,ml,zy).run(TaskMessage())
