from models import db, Lang#, Report
from app import app

#resets, then creates our basic database
db.drop_all()
db.create_all()

#clears the Lang class database
Lang.query.delete()
# Report.query.delete()

#current language objects in our database
english = Lang(name='English', script='English', form_name='Your Name', form_email='Your Email Address', form_phone='Your Phone Number', form_details='Details of the Incident')
chinese = Lang(name='Chinese', script='中文', form_name='你的名字', form_email='您的电子邮件地址', form_phone='你的电话号码', form_details='事故详情')
vietnamese = Lang(name='Vietnamese', script='Tiếng Việt', form_name='Tên của bạn', form_email='Địa chỉ email của bạn', form_phone='Số điện thoại của bạn', form_details='Chi tiết về sự cố')
tagalog = Lang(name='Tagalog', script='Tagalog', form_name='Ang pangalan mo', form_email='Ang iyong email address', form_phone='Iyong numero ng telepono', form_details='Mga Detalye ng Insidente')


db.session.add_all([english, chinese, vietnamese, tagalog])


db.session.commit()

# e_report = Report(form_name='Your Name', form_email='Your Email Address', form_phone='Your Phone Number', form_details='Details of the Incident')
# c_report = Report(form_name='你的名字', form_email='您的电子邮件地址', form_phone='你的电话号码', form_details='事故详情')
# v_report = Report(form_name='Tên của bạn', form_email='Địa chỉ email của bạn', form_phone='Số điện thoại của bạn', form_details='Chi tiết về sự cố')
# t_report = Report(form_name='Ang pangalan mo', form_email='Ang iyong email address', form_phone='Iyong numero ng telepono', form_details='Mga Detalye ng Insidente')

# db.session.add_all([e_report, c_report, v_report, t_report])

# db.session.commit()
