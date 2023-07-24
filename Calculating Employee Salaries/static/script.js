function predictSalaries() {
    var experience_level = document.getElementById("experience_level").value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/predict", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            document.getElementById("result").innerText = "Predicted Salary: " + response.salary;
}

    };
    var data = JSON.stringify({
        "experience_level": experience_level
    });
    xhr.send(data);
}
