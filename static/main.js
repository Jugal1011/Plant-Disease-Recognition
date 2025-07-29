function predict() {
    const fileInput = document.getElementById('imageUpload');
    const file = fileInput.files[0];

    const formData = new FormData();
    formData.append('file', file);

    fetch('/predict', {
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            const resultDiv = document.getElementById('result');
            if (data.error) {
                resultDiv.innerHTML = `Error: ${data.error}`;
            } else {
                resultDiv.innerHTML = `Disease Prediction: ${data.prediction}`;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = 'Error occurred while predicting. Please try again.';
        });
}

document.getElementById('imageUpload').addEventListener('change', function () {
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = ``;
    const file = this.files[0]; // Get the selected file

    if (file) {
        const reader = new FileReader(); // Create a FileReader object

        reader.onload = function (e) {
            const uploadedImage = document.getElementById('uploadedImage');
            uploadedImage.src = e.target.result; // Set the uploaded image source to the FileReader result

            // Show the image preview div
            document.querySelector('.image-preview').style.display = 'block';
        }

        reader.readAsDataURL(file); // Read the image file as a data URL
    }
});