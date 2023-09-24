document.getElementById("filtrujButton").addEventListener("click", function() {
    // Pobierz wybraną opcję filtracji
    const selectedNosnik = document.getElementById("filtrNosnik").value;
  
    // Wyślij zapytanie do serwera z wybraną opcją filtracji
    const xhr = new XMLHttpRequest();
    xhr.open("GET", `/filtruj?nosnik=${selectedNosnik}`, true);
  
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        // Przetworzenie odpowiedzi od serwera
        const wyniki = JSON.parse(xhr.responseText);
        // Tutaj możesz wyświetlić wyniki na stronie
      }
    };
  
    xhr.send();
  });
  