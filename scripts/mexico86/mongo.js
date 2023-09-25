db = connect( 'mongodb://localhost/mexico' );

printjson(db.pays.find({}, {nom:1, _id:0}))

printjson(db.match.find({date:'1986-06-05'}, {paysl: 1, paysv:1, _id:0}))
