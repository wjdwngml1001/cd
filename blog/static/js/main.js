/*document.getElementById('button_click').addEventListener('click', async function(event) {
    event.preventDefault(); // 기본 동작(페이지 이동) 방지

    // 사용자에게 확인을 받음
    const userConsent = confirm('Do you want to access the webcam?');

    // 사용자가 동의한 경우 웹캠 시작
    if (userConsent) {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            const videoElement = document.createElement('video');
            videoElement.srcObject = stream;
            document.body.appendChild(videoElement);
            videoElement.play();
        } catch (error) {
            console.error('Error accessing webcam:', error);
        }
    }
});*/
document.addEventListener('DOMContentLoaded', () => {
    const startButton = document.getElementById('button_click');

    startButton.addEventListener('click', () => {
        // "webcam.html" 페이지로 이동
        window.location.href = 'webcam/';
    });
});