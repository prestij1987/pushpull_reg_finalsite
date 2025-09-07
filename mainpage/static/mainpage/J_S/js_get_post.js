
(function(){
        emailjs.init('sNsoVh8qpiZQwV5ZK'); // Ваш user ID из emailjs
    })();

    const form = document.getElementById('contactForm');
    const responseMessage = document.getElementById('responseMessage');
    const submitBtn = document.getElementById('submitBtn');

    // Валидация email (исправлен RegExp)
    function validateEmail(email) {
        // Было: /^[^s@]+@[^s@]+.[^s@]+$/
        // Исправлено на:
        const re = /^[^s@]+@[^s@]+.[^s@]+$/;
        return re.test(String(email).toLowerCase());
    }

    // Проверка валидности формы вручную
    function validateForm() {
        const name = form.name.value.trim();
        const number = form.number.value.trim();
        const email = form.email.value.trim();
        const message = form.message.value.trim();

        // Было: if (!name  !number  !email || !message) return false;
        // Исправлено на:
        if (!name || !number || !email || !message) return false;

        if (!validateEmail(email)) return false;

        // Проверим телефон по паттерну
        // Было: /^+?d{7,15}$/ - неверный синтаксис
        // Исправлено на:
        const phonePattern = /^+?d{7,15}$/; // от 7 до 15 цифр, опциональный +
        if (!phonePattern.test(number)) return false;

        // Проверка файла (если выбран)
        if(form.file.files.length > 0) {
            const file = form.file.files[0];
            const allowedTypes = ['image/jpeg', 'image/png', 'application/pdf'];
            if (!allowedTypes.includes(file.type)) return false;

            // Проверка размера файла (не более 5MB)
            const maxSizeMB = 5;
            if (file.size > maxSizeMB * 1024 * 1024) return false;
        }

        return true;
    }

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        responseMessage.textContent = '';
        responseMessage.className = '';

        if (!validateForm()) {
            responseMessage.textContent = 'Ошибка: заполните все поля корректно.';
            responseMessage.classList.add('error');
            return;
        }

        submitBtn.disabled = true;

        const templateParams = {
            from_name: form.name.value.trim(),
            phone: form.number.value.trim(),
            from_email: form.email.value.trim(),
            message_html: form.message.value.trim(),
            file_name: form.file.files.length > 0 ? form.file.files[0].name : 'Файл не прикреплен',
            to_email: 'cooper28032023@gmail.com'
        };

        emailjs.send('service_l21xsef', 'template_f27ksbw', templateParams)
            .then(() => {
                responseMessage.textContent = 'Сообщение отправлено.';
                responseMessage.classList.add('success');
                form.reset();
            }, (error) => {
                console.error('FAILED...', error);
                responseMessage.textContent = 'Ошибка при отправке сообщения.';
                responseMessage.classList.add('error');
            })
            .finally(() => {
                submitBtn.disabled = false;
            });
    });