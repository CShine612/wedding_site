//tabs functionality

function setupTabs () {
    document.querySelectorAll(".travel-button").forEach(button => {
        button.addEventListener("click", () => {
            const sideBar = button.parentElement;
            const travelContainer = sideBar.parentElement;
            const clickedTab = button.dataset.forTab;
            const tabToActivate = travelContainer.querySelector('.travel-content[data-tab="' + clickedTab + '"]');

            sideBar.querySelectorAll(".travel-button").forEach(button => {
                button.classList.remove("travel-button-active");
            });

            travelContainer.querySelectorAll(".travel-content").forEach(tab => {
                tab.classList.remove("travel-content-active");
            });

            button.classList.add("travel-button-active")

            tabToActivate.classList.add("travel-content-active")

        })
    })
};

// run tab setup on page load

document.addEventListener("DOMContentLoaded", () => {
    setupTabs()
});

// show pop-up on search click

document.querySelector(".search-button").addEventListener("click", () => {
    const popUp = document.querySelector(".search-pop-up");

    popUp.style.display = "flex";
    
})

document.querySelector(".close").addEventListener("click", () => {
    const popUp = document.querySelector(".search-pop-up");

    popUp.style.display = "none";
})


document.querySelector(".airbnb").addEventListener("click", () => {
    const airBnb = "https://www.airbnb.com/s/Doolin--County-Clare/homes";
    const adults = "?adults=" + document.querySelector("#id_adults").value;
    const children = "&children=" + document.querySelector("#id_children").value;
    const checkin = "&checkin=" + document.querySelector("#id_check_in_year").value + "-" + document.querySelector("#id_check_in_month").value + "-" + document.querySelector("#id_check_in_day").value;
    const checkout = "&checkout=" + document.querySelector("#id_check_out_year").value + "-" + document.querySelector("#id_check_out_month").value + "-" + document.querySelector("#id_check_out_day").value;

    window.open(airBnb + adults + children + checkin + checkout, '_blank').focus();

    console.log(airBnb + adults + children + checkin + checkout);
})

document.querySelector(".hotels").addEventListener("click", () => {
    const hotels = "https://ie.hotels.com/Hotel-Search";
    const adults = "?adults=" + document.querySelector("#id_adults").value;
    const children = "&children=" + document.querySelector("#id_children").value;
    const checkin = "&startDate="  + document.querySelector("#id_check_in_year").value + "-" + document.querySelector("#id_check_in_month").value + "-" + document.querySelector("#id_check_in_day").value;
    const checkout = "&endDate=" + document.querySelector("#id_check_out_year").value + "-" + document.querySelector("#id_check_out_month").value + "-" + document.querySelector("#id_check_out_day").value;
    const destination = "&destination=Doolin%2C%20County%20Clare%2C%20Ireland";

    window.open(hotels + adults + children + checkin + checkout + destination, '_blank').focus();

    console.log(hotels + adults + children + checkin + checkout + destination);
})

document.querySelector(".booking").addEventListener("click", () => {
    const booking = "https://www.booking.com/searchresults.en-gb.html?ss=Doolin&is_ski_area=0&ssne=Doolin&ssne_untouched=Doolin&dest_id=-1502404&dest_type=city";
    const checkin = "&checkin=" + document.querySelector("#id_check_in_year").value + "-" + document.querySelector("#id_check_in_month").value + "-" + document.querySelector("#id_check_in_day").value;
    const checkout = "&checkout=" + document.querySelector("#id_check_out_year").value + "-" + document.querySelector("#id_check_out_month").value + "-" + document.querySelector("#id_check_out_day").value;
    const adults = "&group_adults=" + document.querySelector("#id_adults").value;
    const children = "&group_children=" + document.querySelector("#id_children").value;

    window.open(booking + checkin + checkout + adults + children, '_blank').focus();

    console.log(booking + checkin + checkout + adults + children)

})



