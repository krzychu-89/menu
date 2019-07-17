
function addCell(tr, val) {
var td = document.createElement('td');
td.innerHTML = val;
tr.appendChild(td)
}

function addRow() {
    var tr = document.createElement('tr');
    var tbl = arguments[0];
    for (var i = 1; i < arguments.length; i++) {
        addCell(tr, arguments[i]);
    }
    tbl.appendChild(tr)
}

function generate_menu_table(callback) {
tbl = document.getElementById('dynamic_body');
    for (i = 0; i < menu_data.length; i++){
    addRow(tbl, menu_data[i]['id'], menu_data[i]['name'],
        menu_data[i]['description'], menu_data[i]['num_dishes']);
    }
paginate_table();
}

function paginate_table(){
    $('#dynamic_table_id').smpSortableTable(false, entries_per_page, 'en', {
        tr: {
            onclick:"get_menu_detail(this)",
        },
    })
}


function get_menu_detail(obj){
    array = {};
    var id = obj.getElementsByTagName('td')[0].innerHTML;
    array['id'] = id;
    call_ajax_request(array, 'get_menu_detail', 'POST', function (data){
        //$(".main_div").html(data);
        create_menu_detail_table(data);
    } );
}

function get_menu(){
    array = {};
    //array['id'] = obj.id;
    call_ajax_request(array, 'get_menu', 'POST', function (data){
        //$(".main_div").html(data);
        create_menu_table(data, paginate_table);
    } );
}

function create_menu_table(data, callback){
    var container = document.getElementById('main_div_id');
    $('#main_div_id').empty();
    var tbl = document.createElement("table");
    tbl.className = "table table-bordered";
    tbl.id = "dynamic_table_id";
    var tblBody = document.createElement('tbody');
    var tblHead = document.createElement('thead');
    var h_row = document.createElement("tr");

    var th = document.createElement('th');
    th.innerHTML = "#";
    th.id = "menu_id";
    h_row.appendChild(th);
    var th = document.createElement('th');
    th.innerHTML = "Nazwa";
    th.id = "menu_name";
    h_row.appendChild(th);
    var th = document.createElement('th');
    th.innerHTML = "Opis";
    th.id = "menu_desc";
    th.className = "smp-not-sortable"
    h_row.appendChild(th);
    var th = document.createElement('th');
    th.innerHTML = "Ilość dań";
    th.id = "menu_cnt";
    h_row.appendChild(th);
    var th = document.createElement('th');
    th.innerHTML = "Dodano";
    th.id = "created";
    h_row.appendChild(th);
    var th = document.createElement('th');
    th.innerHTML = "Zmodyfikowano";
    th.id = "modified";
    h_row.appendChild(th);

    tblHead.appendChild(h_row);
    tbl.appendChild(tblHead);
    for (var i=0; i<data.length; i++){
    addRow(tblBody, data[i]['id'], data[i]['name'],
        data[i]['description'], data[i]['num_dishes'],
        data[i]['created'], data[i]['modified']);
    }
    tbl.appendChild(tblBody);
    container.appendChild(tbl);
    callback();
}

function create_menu_detail_table(data){
    var container = document.getElementById('main_div_id');
    $('#main_div_id').empty();
    var tbl = document.createElement("table");
    tbl.className = "table table-bordered";
    tbl.id = "dynamic_table_id";
    var tblBody = document.createElement('tbody');
    var tblHead = document.createElement('thead');
    var h_row = document.createElement("tr");
    var header = ['#', 'Nazwa', 'Opis',
        'Czas przygotowania', 'Danie Wegetariańskie', 'Zdjęcie'];
    for (var i=0; i<header.length; i++){
        addCell(h_row, header[i]);
    }
    tblHead.appendChild(h_row);
    tbl.appendChild(tblHead);
    for (var i=0; i<data.length; i++){
        var img = data[i]['image'];
        if (img !== ""){
            img = '<img src="' + img + '" width="200" height="200" />';
        }
    addRow(tblBody, data[i]['id'], data[i]['name'],
        data[i]['description'], data[i]['preparation_time'],
        data[i]['is_vegetarian'], img);
    }
    tbl.appendChild(tblBody);
    container.appendChild(tbl);
}



jQuery(document).ready(function() {
    //generate_menu_table();
    get_menu();
})