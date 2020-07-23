from models import db, Lang, Report
from app import app

db.drop_all()
db.create_all()

Lang.query.delete()
Report.query.delete()

english = Lang(name='English', script='English')
chinese = Lang(name='Chinese', script='中文')
vietnamese = Lang(name='Vietnamese', script='Tiếng Việt')
tagalog = Lang(name='Tagalog', script='Tagalog')

db.session.add(english)
db.session.add(chinese)
db.session.add(vietnamese)
db.session.add(tagalog)

db.session.commit()

e_report = Report(name='Your Name', email='Your Email Address', phone='Your Phone Number', details='Details of the Incident')
c_report = Report(name='你的名字', email='您的电子邮件地址', phone='你的电话号码', details='事故详情')
v_report = Report(name='Tên của bạn', email='Địa chỉ email của bạn', phone='Số điện thoại của bạn', details='Chi tiết về sự cố')
t_report = Report(name='Ang pangalan mo', email='Ang iyong email address', phone='Iyong numero ng telepono', details='Mga Detalye ng Insidente')

db.session.add_all([e_report, c_report, v_report, t_report])

db.session.commit()