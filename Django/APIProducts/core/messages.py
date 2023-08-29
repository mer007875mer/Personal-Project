def get_status_message(status_code):

    status_messages = {
        200: "عملیات با موفقیت انجام شد.",
        201: "محصول با موفقیت ایجاد شد.",
        400: "داده‌های ارسالی نامعتبرند.",
        403: "توکن معتبر نمیباشد",

    }
    return status_messages.get(status_code, "Unknown Message")