

$(document).ready(function () {
	// filtering products
	$(".filter-checkbox, #priceFilterBtn").on('click', function () {
		//console.log("checkbox clicked!");

		let filterObject = {};

		//get min and max price
		let minPrice = $('#max_price').attr('min');
		let maxPrice = $('#max_price').val();
		// add to filter object
		filterObject.maxPrice = maxPrice;
		filterObject.minPrice = minPrice;

		$(".filter-checkbox").each(function () {
			let filterValue = $(this).val();
			let filterKey = $(this).data("filter");

			//console.log(filterValue, filterKey)
			filterObject[filterKey] = Array.from(document.querySelectorAll('input[data-filter=' + filterKey + ']:checked')).map(function (e) {
				return e.value;
			});
		})
		//console.log(filterObject)

		$.ajax({
			url: '/marketplace/filter-products/',
			data: filterObject,
			dataType: 'json',
			beforeSend: function () {
				console.log('sending data');
			},
			success: function (response) {
				console.log(response);
				$('#filtered-products').html(response.data)
			}
		})
	})

	//price filter limit
	$('#max_price').on('blur', function () {
		let min_price = $(this).attr('min');
		let max_price = $(this).attr('max');
		let current_price = $(this).val();

		min_price = parseFloat(min_price).toFixed(2);
		max_price = parseFloat(max_price).toFixed(2);

		if (current_price > max_price || current_price < min_price) {
			//console.log('Price limit error!')
			alert(`Price must be between ${min_price} and ${max_price}`);
			//$(this).val(minPrice);

		}
	})
})

// 