using assembly System.Windows.Forms
using namespace System.Windows.Forms

$form = [Form] @{
    Text = 'My First PowerShell Form'
}

$button = [Button] @{
    Text = 'Push me'
    Dock = 'Fill'
}

$button.add_click{
    $form.Close()
}

$form.Controls.Add($button)
$form.ShowDialog()