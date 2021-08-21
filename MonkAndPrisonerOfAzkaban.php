<?php
fscanf(STDIN, "%d\n", $n);
$array = trim(fgets(STDIN));
$array = explode(' ', $array);
$lstack = [];
$rstack = [];

$ans = array_fill(0, $n, 0);

for ($i=0; $i<$n; $i++) {
    $pos = $n - $i - 1;
    if ($i == 0) {
        $ans[$i] += -1;
        $ans[$pos] += -1;
    } else {
        while(count($lstack)>0 && $array[end($lstack)-1] <= $array[$i]) {
            array_pop($lstack);
        }
        while(count($rstack)>0 && $array[end($rstack)-1] <= $array[$pos]) {
            array_pop($rstack);
        }
        if (count($lstack) > 0) {
            $ans[$i] += end($lstack);
        } else {
            $ans[$i] += -1;
        }
        if (count($rstack) > 0) {
            $ans[$pos] += end($rstack);
        } else {
            $ans[$pos] += -1;
        }
    }
    $lstack[] = $i+1;
    $rstack[] = $pos+1;
}

echo implode(" ", $ans);
?>
