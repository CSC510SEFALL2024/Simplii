// Wait for document to be ready
$(document).ready(function () {

    var data = [];
    // Populate data from table initially
    $('#myTable tbody tr').each(function () {
        var rowData = [];
        $(this).find('td').each(function () {
            rowData.push($(this).text());
        });
        data.push(rowData);
    });

    // Handle filter changes
    $("#ddlStatus, #ddlCategory, #ddlPriority, #ddlShow").on("change", function () {
        var Status = $('#ddlStatus').find("option:selected").val();
        var Category = $('#ddlCategory').find("option:selected").val();
        var Priority = $('#ddlPriority').find("option:selected").val(); // Get selected Priority
        var Show = $('#ddlShow').find("option:selected").val();
        console.log(Status, Category, Priority, Show);
        SearchData(Show, Status, Category, Priority); // Pass Priority to SearchData function
    });

    // Handle CSV export
    $("#exportCSV").on("click", function() {
        console.log("Export Clicked");
        exportTableToCSV('tasks.csv');
    });
});


// Search/filter function
function SearchData(Show, Status, Category, Priority) {
    if (Status.toUpperCase() == 'ALL' && Category.toUpperCase() == 'ALL' && Priority.toUpperCase() == 'ALL') {
        // Show all rows if Status, Category, and Priority are 'ALL'
        $('#myTable tbody tr').show();
    } else {
        $('#myTable tbody tr:has(td)').each(function () {
            var rowStatus = $.trim($(this).find('td:eq(1)').text());   // Status column
            var rowCategory = $.trim($(this).find('td:eq(2)').text()); // Category column
            var rowPriority = $.trim($(this).find('td:eq(3)').text()); // Priority column

            // Check if the row matches the selected filters
            if (Status.toUpperCase() != 'ALL' && Category.toUpperCase() != 'ALL' && Priority.toUpperCase() != 'ALL') {
                if (rowStatus.toUpperCase() == Status.toUpperCase() && rowCategory == Category && rowPriority.toUpperCase() == Priority.toUpperCase()) {
                    $(this).show();
                } else {
                    $(this).hide();
                }
            } else {
                // Show rows based on any one filter (Status, Category, or Priority)
                if (Status != 'all' && rowStatus.toUpperCase() == Status.toUpperCase()) {
                    $(this).show();
                }
                if (Category != 'all' && rowCategory == Category) {
                    $(this).show();
                }
                if (Priority != 'all' && rowPriority.toUpperCase() == Priority.toUpperCase()) {
                    $(this).show();
                }
                $(this).hide(); // Hide rows that don't match the filters
            }
        });
        $('#myTable tbody tr:visible:gt(' + (Show - 1) + ')').hide();
    }
}


// CSV export functions
function exportTableToCSV(filename) {

    var csv = [];
    var rows = document.querySelectorAll("#myTable tr:visible");
    
    // Get headers
    var headers = [];
    var headerCells = rows[0].querySelectorAll("th");
    for (var i = 0; i < headerCells.length - 4; i++) { // Exclude last 4 columns (Edit, Delete, Reminders, Calendar)
        headers.push(headerCells[i].textContent.trim());
    }
    csv.push(headers.join(","));
    
    // Get visible rows
    for (var i = 1; i < rows.length; i++) {
        var row = [];
        var cols = rows[i].querySelectorAll("td");
        
        // Only include first 5 columns (exclude action buttons)
        for (var j = 0; j < cols.length - 4; j++) {
            var data = cols[j].textContent.trim();
            // Escape commas and quotes
            data = data.replace(/"/g, '""');
            if (data.includes(',')) {
                data = `"${data}"`;
            }
            row.push(data);
        }
        
        csv.push(row.join(","));
    }

    // Download CSV file
    downloadCSV(csv.join("\n"), filename);
}

function downloadCSV(csv, filename) {
    var csvFile = new Blob([csv], {type: "text/csv"});
    var downloadLink = document.createElement("a");
    
    // Create a link to download
    downloadLink.download = filename;
    downloadLink.href = window.URL.createObjectURL(csvFile);
    downloadLink.style.display = "none";
    
    // Add link to DOM and trigger download
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
}