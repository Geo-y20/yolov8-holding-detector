document.addEventListener("DOMContentLoaded", () => {
      console.log("Script loaded and DOM is ready");
  
      const spinner = document.getElementById('spinner');
      if (spinner) {
          spinner.style.display = 'none';
      }
  
      const video = document.getElementById("resultVideo");
      const source = document.getElementById("videoSource");
  
      if (video && source) {
          console.log("Reloading video...");
          video.load(); // Force reload
          video.onloadeddata = () => {
              console.log("Video loaded, attempting to play...");
              video.play().catch((e) => console.warn("Autoplay blocked:", e));
          };
      }
  });
  
  function showSpinner() {
      const spinner = document.getElementById('spinner');
      if (spinner) {
          spinner.style.display = 'block';
      }
  }
  