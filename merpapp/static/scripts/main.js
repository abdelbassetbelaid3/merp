sidbr = document.getElementById('bar');
datatb = document.getElementById('data');
col = datatb.rows



/* for (const row of col) {
    const cells = row.cells;
    cells[0].style.display = 'none';
    cells[0].classList.add("hidden-column")

} */

function openCity(evt, cityName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}


function exportPDF() {

  const element = document.getElementById("data");
  let options = {
    margin: [10, 10, 10, 10], // Set margins to 0 for better content fit
    filename: 'my-styled-report.pdf',
    jsPDF: {
      unit: 'pt', // Set unit to points for finer control (optional)
      // Explore other jsPDF methods for specific styling needs
    }
  };
  html2pdf()
    .from(element)
    .set(options)
    .save();
}


function min(){
    if (sidbr.style.width == '50px'){
        sidbr.style.width = '20%'
        sidbr.style.transitionDuration = '1s'
    }else{
        sidbr.style.width = '50px'
        sidbr.style.transitionDuration = '1s'
    }
     
}
addnew = document.getElementById('addNew')
function addNew(){
  addnew.style.display = 'block';

}
function exportTableToCSV(tableId, filename) {
    const table = document.getElementById(tableId);
    const rows = table.rows;
    let csvContent = "";
  
    // Add header row (optional)
    for (let i = 0; i < rows[0].cells.length; i++) {
      if (!rows[0].cells[i].classList.contains("hidden-column")) { // Check if cell is not hidden
        const cellText = rows[0].cells[i].innerText;
        csvContent += cellText + (i < rows[0].cells.length - 1 ? ',' : '\n'); // Add comma separator except for last cell
      }
    }
  
    // Add data rows
    for (let i = 1; i < rows.length; i++) {
      let rowData = ""; // String to store data for the current row
      for (let j = 0; j < rows[i].cells.length; j++) {
        if (!rows[i].cells[j].classList.contains("hidden-column")) { // Check if cell is not hidden
          const cellText = rows[i].cells[j].innerText;
          rowData += cellText + (j < rows[i].cells.length - 1 ? ',' : ''); // Add comma separator except for last cell
        }
      }
      csvContent += rowData + '\n';
    }
  
    const link = document.createElement('a');
    link.href = 'data:text/csv;charset=utf-8,' + encodeURIComponent(csvContent);
    link.download = filename || 'table_data.csv';
    link.click();
}

function show_options(){
    filter_options = document.getElementById('options');
    filter_options.style.display = 'block';
}

function filter_options(){
  alert(1)
  options = document.getElementById('filter')
  if(options.checked){
    alert(2)
  }
}