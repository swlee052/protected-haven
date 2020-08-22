from models import db, Lang, Resource
from app import app

#resets, then creates our basic database
db.drop_all()
db.create_all()

#clears the Lang class database
Lang.query.delete()
# Report.query.delete()

#current language objects in our database
english = Lang(name='English',
                script='English',
                form_name='Name',
                form_email='Email Address',
                form_phone='Phone Number',
                form_details='Details of the Incident',
                form_geoloc="Do not send location",
                form_personal_info="Personal Information (optional)",
                form_incident_details="Details of Incident",
                form_submit="Submit",
                form_cancel="Cancel",
                form_resources="Resources",
                form_no_geo='Do not send location')
chinese = Lang(name='Chinese',
                    script='中文',
                    form_name='你的名字',
                    form_email='您的电子邮件地址',
                    form_phone='你的电话号码',
                    form_details='事故详情',
                    form_geoloc="不发送位置",
                    form_personal_info="个人信息（可选）",
                    form_incident_details="事故详情",
                    form_submit="提交",
                    form_cancel="取消",
                    form_resources="资源资源",
                    form_no_geo='不发送位置')
vietnamese = Lang(name='Vietnamese',
                    script='Tiếng Việt',
                    form_name='Tên của bạn',
                    form_email='Địa chỉ email của bạn',
                    form_phone='Số điện thoại của bạn',
                    form_details='Chi tiết về sự cố',
                    form_geoloc="Không gửi vị trí",
                    form_personal_info="Thông tin cá nhân (Tùy chọn)", 
                    form_incident_details="Chi tiết về sự cố",
                    form_submit="Gửi đi",
                    form_cancel="Huỷ bỏ",
                    form_resources="Không gửi vị trí",
                    form_no_geo='Do not send location')
tagalog = Lang(name='Tagalog', script='Tagalog',
                form_name='Ang pangalan mo',
                form_email='Ang iyong email address',
                form_phone='Iyong numero ng telepono',
                form_details='Mga Detalye ng Insidente',
                form_geoloc="Huwag magpadala ng lokasyon",
                form_personal_info="Personal na Impormasyon (Opsyonal)",
                form_incident_details="Mga Detalye ng Insidente",
                form_submit="Ipasa",
                form_cancel="Pagkansela",
                form_resources="Mga mapagkukunan",
                form_no_geo='Huwag magpadala ng lokasyon')


db.session.add_all([english, chinese, vietnamese, tagalog])


db.session.commit()

Resource.query.delete()

eng = Lang.query.get_or_404('English')

test_resource = Resource(title="test", text="test", phone='1-800-222-3333', email='test@test.com', address='Neverland')

db.session.add(test_resource)
db.session.commit()

resource = Resource.query.get(1)

eng.resources.append(resource)

db.session.commit()

