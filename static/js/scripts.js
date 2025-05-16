
function previewImage(event) {
    let reader = new FileReader();
    reader.onload = function() {
        let preview = document.getElementById('image-preview');
        preview.src = reader.result;
        document.getElementById('image-preview-container').classList.remove('hidden');
    }
    reader.readAsDataURL(event.target.files[0]);
}

function copyToClipboard(color) {
    navigator.clipboard.writeText(color);
    alert("Copied: " + color);
}