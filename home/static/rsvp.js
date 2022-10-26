document.querySelectorAll("#id_attending_0").forEach((groupMember, i) => {
    groupMember.addEventListener("click", () => {
        infoSection = document.querySelectorAll(".info")[i];
        infoSection.style.display = "block";
    })
})

document.querySelectorAll("#id_attending_1").forEach((groupMember, i) => {
    groupMember.addEventListener("click", () => {
        infoSection = document.querySelectorAll(".info")[i];
        infoSection.style.display = "none";
    })
})

document.querySelectorAll("#id_plus_one_attendance_0").forEach((groupMember, i) => {
    groupMember.addEventListener("click", () => {
        console.log("click yes")
        plusOneSection = document.querySelectorAll(".plus-one-form")[i];
        plusOneSection.style.display = "block";
    })
})

document.querySelectorAll("#id_plus_one_attendance_1").forEach((groupMember, i) => {
    groupMember.addEventListener("click", () => {
        console.log("click no")
        plusOneSection = document.querySelectorAll(".plus-one-form")[i];
        plusOneSection.style.display = "none";
    })
})