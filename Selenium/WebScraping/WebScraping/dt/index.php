<?php

require_once("connection.php");
$query = "SELECT id, airlift_product.product_name, airlift_category.category_name,`price`, airlift_image.image_link, airlift_links.link_value,`coin`,`orignal_price`,`discount_percentage`, airlift_stock.stock_value, airlift_location.location_name, source.source_name, `update_time` FROM (((((((airlift INNER JOIN airlift_stock ON airlift.product_avalible = airlift_stock.stock_id) INNER JOIN airlift_product ON airlift.name = airlift_product.product_id) INNER JOIN airlift_location ON airlift.location = airlift_location.location_id) INNER JOIN airlift_links ON airlift.link = airlift_links.link_id) INNER JOIN airlift_image ON airlift.image = airlift_image.image_id) INNER JOIN airlift_category ON airlift.category = airlift_category.category_id) INNER JOIN source ON airlift.source = source.source_id) WHERE update_time >= ( CURDATE() - INTERVAL 1 DAY )  ORDER BY `id` DESC";
$result = mysqli_query($con, $query);

?>
<!DOCTYPE html>
<html>

<head>
	<meta charset="utf-8">
	<link rel="shortcut icon" type="image/ico" href="http://www.datatables.net/favicon.ico">
	<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1.0, user-scalable=no">
	<title>DataTables example - Zero configuration</title>
	<link rel="stylesheet" type="text/css" href="media/css/jquery.dataTables.css">
	<link rel="stylesheet" type="text/css" href="resources/syntax/shCore.css">
	<link rel="stylesheet" type="text/css" href="resources/demo.css">
	<style type="text/css" class="init">

	</style>
	<script type="text/javascript" language="javascript" src="https://code.jquery.com/jquery-3.5.1.js"></script>
	<script type="text/javascript" language="javascript" src="media/js/jquery.dataTables.js"></script>
	<script type="text/javascript" language="javascript" src="resources/syntax/shCore.js"></script>
	<script type="text/javascript" language="javascript" src="resources/demo.js"></script>
	<script type="text/javascript" language="javascript" class="init">
		$(document).ready(function() {
			$('#example').DataTable();
		});
	</script>
</head>

<body class="dt-example px-3">
	<div class="container-fluid">
		<section>
			<div class="demo-html"></div>
			<table id="example" class="display" style="width:100%">
				<thead>
					<tr>
						<th> ID </th>
						<th> Image </th>
						<th> Name </th>
						<th> Catogory </th>
						<th> Price </th>
						<th> Coin </th>
						<th> Orignal Price </th>
						<th> Discount </th>
						<th> Change </th>
						<th> Availiablilty </th>
						<th> location </th>
						<th> Source </th>
						<th> Time </th>
					</tr>
				</thead>
				<tbody>
					<?php
					while ($row = mysqli_fetch_assoc($result)) {
						// print_r($row);
						$id = $row['id'];
						$image = $row['image_link'];
						$name = $row['product_name'];
						$category = $row['category_name'];
						$price = $row['price'];
						$link = $row['link_value'];
						$coin = $row['coin'];
						$orignal_price = $row['orignal_price'];
						$discount = $row['discount_percentage'];
						$available = $row['stock_value'];
						$location = $row['location_name'];
						$source = $row['source_name'];
						$update_time = $row['update_time'];
					?>
						<tr>
							<td><?php echo $id ?></td>
							<td><img src="<?php echo $image ?>" alt="image" width="50" height="50"></td>
							<td><a href="<?php echo $link ?>"><?php echo $name ?></a></td>
							<td><?php echo $category ?></td>
							<td><?php echo $price ?></td>
							<td><?php echo $coin ?></td>
							<td><?php echo $orignal_price ?></td>
							<td><?php echo $discount ?></td>
							<td><?php echo $orignal_price - $price ?></td>
							<td><?php echo $available ?></td>
							<td><?php echo $location ?></td>
							<td><?php echo $source ?></td>
							<td><?php echo $update_time ?></td>
						</tr>
					<?php
					}
					?>
				</tbody>
				<tfoot>
					<tr>
						<th> ID </th>
						<th> Image </th>
						<th> Name </th>
						<th> Catogory </th>
						<th> Price </th>
						<th> Coin </th>
						<th> Orignal Price </th>
						<th> Discount </th>
						<th> Change </th>
						<th> Availiablilty </th>
						<th> location </th>
						<th> Source </th>
						<th> Time </th>
					</tr>
				</tfoot>
			</table>
		</section>
	</div>
</body>

</html>