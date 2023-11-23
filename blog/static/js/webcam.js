
document.addEventListener('DOMContentLoaded', async () => {
    const webcamContainer = document.getElementById('webcam-container');

    try {
        // 권한 요청
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });

        // 웹캠이 허용된 경우, 스트림을 비디오로 표시
        const videoElement = document.createElement('video');
        videoElement.srcObject = stream;

        // 비디오를 컨테이너에 추가
        webcamContainer.appendChild(videoElement);

        // 비디오 재생 시작
        videoElement.play();

        // face-api.js 설정
        await faceapi.nets.tinyFaceDetector.loadFromUri('https://cdn.jsdelivr.net/npm/face-api.js@2.0.11/weights');
        await faceapi.nets.faceLandmark68Net.loadFromUri('https://cdn.jsdelivr.net/npm/face-api.js@2.0.11/weights');
        await faceapi.nets.faceRecognitionNet.loadFromUri('https://cdn.jsdelivr.net/npm/face-api.js@2.0.11/weights');
        
        // 얼굴 인식 및 크롭
        videoElement.addEventListener('play', async () => {
            const canvas = faceapi.createCanvasFromMedia(videoElement);
            webcamContainer.appendChild(canvas);

            const displaySize = { width: videoElement.width, height: videoElement.height };
            faceapi.matchDimensions(canvas, displaySize);

            setInterval(async () => {
                const detections = await faceapi.detectAllFaces(videoElement, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceDescriptors();
                const resizedDetections = faceapi.resizeResults(detections, displaySize);
                canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
                faceapi.draw.drawDetections(canvas, resizedDetections);

                if (detections.length > 0) {
                    // 얼굴이 감지된 경우, 크롭 등의 추가 작업 수행 가능
                    const croppedImage = await faceapi.extractFaces(videoElement, detections);
                }
            }, 100);
        });
    } catch (error) {
        console.error('Error accessing webcam:', error);
    }
});