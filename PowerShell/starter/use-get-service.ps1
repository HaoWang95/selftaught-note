$allServices = Get-Service;

$stopped = $allServices | Where-Object Status -EQ 'Stopped';
$running = $allServices | Where-Object Status -EQ 'Running';


Write-Output $stopped
Write-Output $running;

