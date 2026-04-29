document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('#registerForm');
  if (!form) {
    return;
  }

  const fileInput = form.querySelector('input[type="file"]');
  const dropZone = document.querySelector('#avatarDropZone');
  const caption = document.querySelector('#avatarCaption');
  const preview = document.querySelector('#avatarPreview');
  const previewImage = document.querySelector('#avatarPreviewImage');
  const removeBtn = document.querySelector('#avatarRemoveBtn');

  if (fileInput && caption && preview && previewImage && dropZone) {
    const setFile = (file) => {
      if (!file) {
        caption.textContent = 'Файл не выбран';
        preview.classList.remove('is-visible');
        previewImage.removeAttribute('src');
        dropZone.classList.remove('is-error');
        return;
      }

      if (!file.type.startsWith('image/')) {
        caption.textContent = 'Только изображения (JPG, PNG, WEBP)';
        dropZone.classList.add('is-error');
        preview.classList.remove('is-visible');
        previewImage.removeAttribute('src');
        return;
      }

      dropZone.classList.remove('is-error');
      caption.textContent = file.name;
      const blobUrl = URL.createObjectURL(file);
      previewImage.src = blobUrl;
      preview.classList.add('is-visible');
    };

    fileInput.addEventListener('change', () => {
      const file = fileInput.files && fileInput.files[0];
      setFile(file);
    });

    ['dragenter', 'dragover'].forEach((eventName) => {
      dropZone.addEventListener(eventName, (event) => {
        event.preventDefault();
        dropZone.classList.add('is-dragover');
      });
    });

    ['dragleave', 'drop'].forEach((eventName) => {
      dropZone.addEventListener(eventName, (event) => {
        event.preventDefault();
        dropZone.classList.remove('is-dragover');
      });
    });

    dropZone.addEventListener('drop', (event) => {
      const file = event.dataTransfer && event.dataTransfer.files && event.dataTransfer.files[0];
      if (!file) {
        return;
      }

      const dt = new DataTransfer();
      dt.items.add(file);
      fileInput.files = dt.files;
      setFile(file);
    });

    if (removeBtn) {
      removeBtn.addEventListener('click', () => {
        fileInput.value = '';
        setFile(null);
      });
    }
  }

  const controls = form.querySelectorAll('input, textarea, select');
  controls.forEach((el) => {
    const toggleFilled = () => {
      const hasValue = Boolean(el.value && el.value.trim());
      el.classList.toggle('is-filled', hasValue);
    };

    toggleFilled();
    el.addEventListener('input', toggleFilled);
    el.addEventListener('change', toggleFilled);
  });
});
