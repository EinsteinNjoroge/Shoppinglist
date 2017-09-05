function setWindowHeight() {
    $('.mid-center').css('height', $(window).height());
}


$(document).ready(function () {

    setWindowHeight();
    $(window).resize(function () {
        setWindowHeight();
    })

    // initialize jquery datatable on the shoppinglist
    $("#shoppinglistTable").DataTable({
        "paging": false,
        "info": false,
        columns: [
            {title: "Priority"},
            {title: "When I go to the store, I'll buy.."},
            {title: "Action"}
        ]
    });

    // initialize jquery datatable on shoppinglist items
    $("#shoppingListItemsTable").DataTable({
        "paging": false,
        "info": false,
        columns: [
            {title: "Item"},
            {title: "Action"}
        ]
    });

    // initialize click listener on edit button
    let editBtn = $(".edit-btn");
    editBtn.click(function () {
        let currentRow = $(this).parents("tr");

        // remove event listeners on this row
        $(this).parents("tr").find("[data-ref]").off();

        // get id for the parent row and parent table
        let currentRowID = $(this).parents("tr").attr("id");
        let currentTable = $(this).parents("table");
        let currentTableID = $(currentTable).attr("id");

        // get data values from this row
        let currentTableRow = $("#" + currentTableID).DataTable().row(currentRow);
        let values = currentTableRow.data();

        // define an editor for each datatable
        let editor = null;
        if (currentTableID === "shoppinglistTable") {
            editor = [
                "<input type=\"hidden\" name=\"id\" value=\"" + currentRowID + "\" />",
                "<textarea name=\"title\">" + values[1] + "</textarea>",
                "<button class=\"btn btn-primary\">Save</button>"
            ];
        } else if (currentTableID === "shoppingListItemsTable") {
            editor = [
                "<input type=\"hidden\" name=\"id\" value=\"" + currentRowID + "\" />" +
                "<textarea name=\"name\">" + values[0] + "</textarea>",
                "<button class=\"btn btn-primary\">Save</button>"
            ];
        }

        // update the UI with the editors
        currentTableRow.data(editor).draw();
    });

    // initialize click listener on delete button
    let deleteBtn = $(".delete-btn");
    deleteBtn.click(function () {
        let referenceLink = $(this).attr("delete-ref");

        // PopUp a confirmation dialog
        $.confirm({
            title: "Remove!",
            content: "Do you really want to remove this!",
            buttons: {
                remove: {
                    btnClass: "btn-danger",
                    action() {
                        window.location.href = referenceLink;
                    }
                },
                cancel: {
                    btnClass: "btn-blue"
                }
            }
        });
    });

    // initialize click listener on delete elements with attribute `data-ref`
    let referenceLink = $("[data-ref]");
    referenceLink.click(function () {

        // redirect to new url
        window.location.href = $(this).attr("data-ref");
    });

});
