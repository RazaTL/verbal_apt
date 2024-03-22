let mediaRecorder;
let chunks = [];

function recordAndSaveAudio() {
    if (!mediaRecorder || mediaRecorder.state === 'inactive') {
        // Start recording
        navigator.mediaDevices.getUserMedia({ audio: true })
            .then(stream => {
                mediaRecorder = new MediaRecorder(stream);
                chunks = [];

                mediaRecorder.ondataavailable = event => {
                    chunks.push(event.data);
                };

                mediaRecorder.onstop = () => {
                    const blob = new Blob(chunks, { type: 'audio/wav' });
                    const url = URL.createObjectURL(blob);

                    // Create a download link for the audio file
                    const downloadLink = document.createElement('a');
                    downloadLink.href = url;
                    downloadLink.download = 'recorded_audio.wav';
                    document.body.appendChild(downloadLink);
                    
                    // Click the download link to trigger the download
                    downloadLink.click();

                    // Clean up
                    chunks.length = 0;
                    URL.revokeObjectURL(url);
                };

                mediaRecorder.start();
            })
            .catch(error => {
                console.error('Error accessing microphone:', error);
            });
    } else {
        // Stop recording
        mediaRecorder.stop();
    }
}