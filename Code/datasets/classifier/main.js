function handleDirectoryInput(event) {
  const files = event.target.files;

  // // List the files from the directory
  // for (let i = 0; i < files.length; i++) {
  //   const path = files[i].webkitRelativePath || files[i].name;
  //   console.log('file-path', files[i]);
  // }

  const gallery = document.getElementById('image-gallery');
  gallery.innerHTML = '';  // Clear the gallery

  // Filter files to include only images
  const imageTypes = ['image/jpeg', 'image/png', 'image/gif'];
  for (const file of files) {
    if (imageTypes.includes(file.type)) {
      const img = document.createElement('img');
      img.src = URL.createObjectURL(file);
      img.style.width = '200px';  // Adjust size as needed
      img.onload = () => URL.revokeObjectURL(img.src);  // Clean up URL after loading
      gallery.appendChild(img);
    }
  }
}

window.handleDirectoryInput = handleDirectoryInput;
window.onload = () => {
  // document.querySelector('')
}