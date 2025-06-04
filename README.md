# Private_car_carpooling_app

前端主要界面：登陆注册界面、主界面、分享共享行程界面、查看共享行程界面、订单界面、具体行程界面。

登录注册界面：完成用户注册、用户登录后进入主界面。

主界面：底部有功能栏（可切换“出行”、“个人”）。出行界面显示“分享共享行程”“查看共享行程”“订单”按钮进入对应功能。个人主页界面显示个人信息，并有“个人信息修改”“司机认证”功能栏可点击进入。

分享共享行程界面（已进行司机认证的私家车车主点击后进入，否则点击后显示“非私家车车主”）：可填写行程时间、可共享人数、共享车牌号（从已认证的私家车选择）、共享的起始位置、共享的终止位置、预估车费。填写完成后有确认按钮，点击后跳转到具体行程界面。

查看共享行程界面（想要拼车的用户可进入）：上方有筛选栏对共享行程列表筛选，下方显示共享行程列表，包括行程时间、可共享人数、共享起始位置、共享终止位置、行程状态，并且每个行程有详情按钮，点击后可以查看到行程具体信息（同具体行程界面现实的信息），并且有“拼车”按钮，点击后跳转到具体行程界面，切换行程状态。

订单界面：显示订单列表（用户作为私家车车主的订单和作为乘客的订单），标注订单号、行程状态，点击“详情”跳转到具体行程界面。

具体行程界面：显示当前共享行程的订单号、共享私家车主、联系电话、行程时间、可共享人数、共享车牌号、共享起始位置、共享终止位置、预估车费、行程状态（未拼车，拼车失败，已拼车，行程进行中，已完成）。乘客点击“开始行程”表示已上车，切换行程状态，点击“已完成”表示行程结束，切换行程状态，跳转到支付界面。

前端：Vue 3 + Vue Router + Axios + Element Plus
后端：Flask + Flask-JWT-Extended + Flask-SQLAlchemy
数据库：MySQL
接口风格：RESTful API

文件结构(预期)：
Private_car_carpooling_app/
│
├── backend/
│   ├── app.py                  # 主应用入口
│   ├── models.py               # ORM模型
│   ├── app/                        #app模块
│   │   ├──  __init__.py          #创建 app + 注册扩展
│   │   ├── routes/                #路由模块
│   │   │   ├── login.py             # 登录注册接口
│   │   │   ├── user.py             # 用户信息、司机认证
│   │   │   ├── trip.py              # 行程发布/查询/详情
│   │   │   └──order.py             # 订单相关
│   └── config.py                   #配置类
├── frontend/
│   ├── node_modules/             # 第三方包存储目录
│   ├── public/           #任何放置在 public 文件夹的静态资源都会被简单的复制，而不经过 webpack
│   │   ├── favicon.ico           浏览器收藏夹图标
│   │   └──index.html            单页面 HTML 文件
│   ├── src/
│   │   ├── assets/                #公共资源目录，放图片等资源
│   │   ├── components/            #公共组件目录
│   │   │   └── TopNav.vue                  # 顶部导航栏，显示用户名，有“返回”“首页”两个按钮
│   │   ├── router/              #路由模块
│   │   │   └── index.js                  # Vue Router 配置
│   │   ├── store/                # Vue 容器模块
│   │   ├── api/
│   │   │   └── index.js                  # axios 实例配置，统一设置 baseURL
│   │   ├── views/                #视图组件存储目录，所有的路由页面都存储到这里
│   │   │   ├── Login.vue                  #登录界面
│   │   │   ├── Register.vue             #注册界面
│   │   │   ├── Home.vue                 #主界面
│   │   │   ├── TripForm.vue              # 发布共享行程界面表单
│   │   │   ├── TripList.vue              # 行程列表
│   │   │   ├── TripDetail.vue            # 行程详情页
│   │   │   ├── OrderList.vue             # 订单列表
│   │   │   ├── PersonalInfo.vue          # 个人信息页
│   │   │   └── DriverAuth.vue            # 司机认证页
│   │   ├──App.vue               #根组件，最终被替换渲染到 index.html 页面中 #app 入口节点
│   │   └──main.js               #整个项目的启动入口模块
│   ├── ……



数据库（已创建的表如下，名称、密码见config.py）
create table USERS(
id int primary key not null,
name varchar(255) not null,
password varchar(255) not null,
phone char(11) not null,
email varchar(255)
);

create table DRIVER(
driver_id int primary key not null,
carnumber varchar(50) not null,
id int not null,
name varchar(255) not null,
phone char(11) not null,
foreign key(id) references USERS(id)
);

create table TRIP(
order_id int primary key not null,
driver_id int not null,
passenger_id int,
time timestamp not null,
person int not null,
pickup_location varchar(255) not null,
dropof_location varchar(255) not null,
money int not null,
status varchar(10) not null,
foreign key(driver_id) references DRIVER(driver_id),
foreign key(passenger_id) references USERS(id)
);
