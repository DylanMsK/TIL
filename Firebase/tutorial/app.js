db.collection('cafes').get().then((snapshot) => {
    console.log(snapshot.docs);
})