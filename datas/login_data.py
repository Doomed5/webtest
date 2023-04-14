

class LoginData:
    success_case_data = [
        {'mobile': 'wagyu2016@163.com', 'pwd': 'admin123456', 'excepted': '登录成功'}
    ]
    error_case_data = [
        {'mobile': 'wagyu2016@163.com', 'pwd': '', 'excepted': '请输入密码'}
    ]
    error_alert_data = [
        {'mobile': 'wagyu2018@163.com', 'pwd': 'admin123456', 'excepted': '用户不存在'},
        {'mobile': 'wagyu2018@163.com', 'pwd': '12345', 'excepted': '密码有效长度是6到30个字符'},
        {'mobile': 'wagyu2018@163.com', 'pwd': '0123456789012345678901234567891', 'excepted': '密码有效长度是6到30个字符'}
    ]
