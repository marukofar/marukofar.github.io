![](images/day6.png)

# PHP error_reporting()
`error_reporting()` ใช้สำหรับแสดงข้อผิดพลาด (Error) ของโปรแกรม PHP โดยแสดงว่ามีข้อผิดพลาดอะไร เพื่อ Dev สามารถแก้ไขได้ง่ายและถูกจุด สะดวกต่อการทำ Debug ในด้าน Security หากข้อผิดพลาดเกิดไปแสดงต่อผู้ไม่ประสงค์ดี สามารถนำไปสู่การแฮกได้  

### รูปแบบการใช้งาน

```php 
error_reporting ( int $level = ? ) : int
```

### Parameters 

- `level` - 

### การคืนค่า

จะคืนค่า level ของ`error_reporting` ก่อนหน้า หรือ level ปัจจุบันหากไม่มีการกำหนด level parameter

### ตัวอย่างการใช้ `error_reporting()`

### ตัวอย่างแบบที่ 1 

```php 
<?php

// Turn off all error reporting
error_reporting(0);

// Report simple running errors
error_reporting(E_ERROR | E_WARNING | E_PARSE);

// Reporting E_NOTICE can be good too (to report uninitialized
// variables or catch variable name misspellings ...)
error_reporting(E_ERROR | E_WARNING | E_PARSE | E_NOTICE);

// Report all errors except E_NOTICE
error_reporting(E_ALL & ~E_NOTICE);

// Report all PHP errors (see changelog)
error_reporting(E_ALL);

// Report all PHP errors
error_reporting(-1);

// Same as error_reporting(E_ALL);
ini_set('error_reporting', E_ALL);

?>
```
### ตัวอย่างแบบที่ 2 ใช้จัดการข้อผิดพลาด (Error) ในสคริปต์

```php
<?php
// we will do our own error handling
error_reporting(0);

// user defined error handling function
function userErrorHandler($errno, $errmsg, $filename, $linenum, $vars) {
    // timestamp for the error entry
    $dt = date("Y-m-d H:i:s (T)");

    // define an assoc array of error string
    // in reality the only entries we should
    // consider are 2,8,256,512 and 1024
    $errortype = array (
                1    =>  "Error",
                2    =>  "Warning",
                4    =>  "Parsing Error",
                8    =>  "Notice",
                16   =>  "Core Error",
                32   =>  "Core Warning",
                64   =>  "Compile Error",
                128  =>  "Compile Warning",
                256  =>  "User Error",
                512  =>  "User Warning",
                1024 =>  "User Notice"
                );
    // set of errors for which a var trace will be saved
    $user_errors = array(E_USER_ERROR, E_USER_WARNING, E_USER_NOTICE);
    
    $err = "<errorentry>\n";
    $err .= "\t<datetime>" . $dt . "</datetime>\n";
    $err .= "\t<errornum>" . $errno . "</errornum>\n";
    $err .= "\t<errortype>" . $errortype[$errno] . "</errortype>\n";
    $err .= "\t<errormsg>" . $errmsg . "</errormsg>\n";
    $err .= "\t<scriptname>" . $filename . "</scriptname>\n";
    $err .= "\t<scriptlinenum>" . $linenum . "</scriptlinenum>\n";

    if (in_array($errno, $user_errors))
        $err .= "\t<vartrace>" . wddx_serialize_value($vars, "Variables") . "</vartrace>\n";
    $err .= "</errorentry>\n\n";
    
    // for testing
    // echo $err;

    // save to the error log, and e-mail me if there is a critical user error
    error_log($err, 3, "/usr/local/php4/error.log");
    if ($errno == E_USER_ERROR)
        mail("phpdev@example.com", "Critical User Error", $err);
}


function distance($vect1, $vect2) {
    if (!is_array($vect1) || !is_array($vect2)) {
        trigger_error("Incorrect parameters, arrays expected", E_USER_ERROR);
        return NULL;
    }

    if (count($vect1) != count($vect2)) {
        trigger_error("Vectors need to be of the same size", E_USER_ERROR);
        return NULL;
    }

    for ($i=0; $i<count($vect1); $i++) {
        $c1 = $vect1[$i]; $c2 = $vect2[$i];
        $d = 0.0;
        if (!is_numeric($c1)) {
            trigger_error("Coordinate $i in vector 1 is not a number, using zero",
                            E_USER_WARNING);
            $c1 = 0.0;
        }
        if (!is_numeric($c2)) {
            trigger_error("Coordinate $i in vector 2 is not a number, using zero",
                            E_USER_WARNING);
            $c2 = 0.0;
        }
        $d += $c2*$c2 - $c1*$c1;
    }
    return sqrt($d);
}

$old_error_handler = set_error_handler("userErrorHandler");

// undefined constant, generates a warning
$t = I_AM_NOT_DEFINED;

// define some "vectors"
$a = array(2, 3, "foo");
$b = array(5.5, 4.3, -1.6);
$c = array (1, -3);

// generate a user error
$t1 = distance($c, $b) . "\n";

// generate another user error
$t2 = distance($b, "i am not an array") . "\n";

// generate a warning
$t3 = distance($a, $b) . "\n";

?> 
```


#### Reference
- https://www.php.net/manual/en/function.error-reporting.php
- https://www.macs.hw.ac.uk/~hwloidl/docs/PHP/ref.errorfunc.html#e-error
