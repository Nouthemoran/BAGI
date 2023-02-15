<?php
include("koneksi-tutor.php");

// Fetch all users data from database
$sql = "SELECT * FROM mahasiswa";
$result = mysqli_query($conn, $sql);

?>

<!DOCTYPE html>
<html>
<head>
	<title>View Data Mahasiswa</title>
</head>

<body>
	<h2>Data Mahasiswa</h2>

	<a href="action-input-data.php">Tambah Data Baru</a><br/><br/>

	<table width='80%' border=1>

	<tr>
		<th>NIM</th> <th>Nama</th> <th>Jurusan</th> <th>Alamat</th> <th>Telepon</th> <th>Update</th>
	</tr>
	
	<?php
	while($user_data = mysqli_fetch_array($result)) { ?>
	<tr>
		<td><?php echo $user_data['id_mahasiswa']; ?></td>
		<td><?php  echo $user_data['nama'] ?></td>
		<td><?php echo $user_data['jurusan'] ?></td>
		<td><?php echo $user_data['alamat'] ?></td>
		<td><?php echo $user_data['telepon'] ?></td>
		<td><a href='edit.php?id=$user_data[id]'>Edit</a> | <a href='delete.php?id=$user_data[id]'>Delete</a></td>
    </tr>
	<?php } ?>



	</table>
</body>
</html>
