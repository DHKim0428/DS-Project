const functions = require('firebase-functions');
const admin = require('firebase-admin');
const request = require('request');
admin.initializeApp(functions.config().firebase);

// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//
// exports.helloWorld = functions.https.onRequest((request, response) => {
//  response.send("Hello from Firebase!");
// });

exports.sendNotification = functions.database.ref('GN/{timestamp}').onCreate((snap, context) => {
    console.log('event data: ', snap);
    console.log('event.data.val()' + snap.val().title);

    const dataVal = snap.val();
    if(!dataVal){
        return console.log('Message data null!');
    }
    const title = dataVal.title;
    const url = dataVal.url;
    const promiseUserList = admin.database().ref('Users/').once('value');
    const arrUserList = [];
    return Promise.all([promiseUserList]).then(results => {
        console.log(results);
        if(results[0].hasChildren()){
            results[0].forEach(snapshot => {
                console.log(snapshot.key);
                arrUserList.push(snapshot.key);
            });
            console.log(arrUserList);
        }else{
            console.log('UserList is null');
        }

        for (let i=0; i<arrUserList.length; i++) {
            console.log(`FcmId/${arrUserList[i]}`);
            admin.database().ref(`FcmId/${arrUserList[i]}`).once('value', fcmSnapshot => {
                console.log('FCM Token:', fcmSnapshot.val());
                const token = fcmSnapshot.val();
                if (token) {
                    const payload = {
                        notification: {
                            title: "새 글이 올라왔어요!",
                            body: title,
                            click_action: "https://ksacombined.cf/?gn=1",
                            icon: ""
                        }
                    };
                    admin.messaging().sendToDevice(token, payload).then(response => {
                        response.results.forEach((result, index) => {
                            const error = result.error;
                            if (error) {
                                console.log('FCM 실패 :', error.code);
                            } else {
                                console.log('FCM 성공');
                            }
                        });
                    });
                }
            });
        }
    });
});

exports.sendHaksa = functions.https.onRequest((req, res)=>{
    let options = {
        headers: {'Content-Type': 'application/json'},
        url: "http://klist.cf:54321/info",
        body: JSON.stringify(req.body)
    };
    //res.status(200).send('<script>alert("Finish");</script>');
    request.post(options, (err, response, results)=>{
        if(err){
            res.send('hello');
        }else{
            res.status(200).send('<script>alert("' + results + '");</script>');
        }
    })
});

exports.sendJena = functions.https.onRequest((req, res)=>{
    let options = {
        headers: {'Content-Type': 'application/json'},
        url: "https://gaonnuri.ksain.net/Jena/kakaotalk/message.php",
        body: JSON.stringify(req.body)
    };
    request.post(options, (err, response, results)=>{
        if(err){
            res.send('err');
        }else{
            console.log(response);
            console.log(results);
            res.status(200).send(results);
        }
    })
});


exports.updateGN = functions.https.onRequest((req, res)=>{
    if(req.body.title && req.body.url){
        let t = Date.now()
        admin.database().ref('GN/' + t).set({
            title: req.body.title,
            url: req.body.url
        })
    }
    res.send('<h1>Test Page</h1>');
});

