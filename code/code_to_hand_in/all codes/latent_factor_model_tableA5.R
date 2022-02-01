#### general imports
#install.packages('C:/Users/fx236/Documents/AME_files/R/phtt', repos = NULL, type ='source')
#install.packages('haven')
library("phtt")
library('haven')
#### full data  yearly latent factors
raw_data = read_dta("C:/Users/fx236/Documents/AME_files/data_court decisions/Data/final/matched.dta")
data = raw_data[0:269268,]
dim(data)
n <- 67317; T <- 4
print(n*T)
res <- matrix(data$res,n,T)
temp6t410  <- data$temp6t4/1000
temp6t410 <- matrix(temp6t410,n,T)
dim(temp6t410)
press6t4 <- matrix(data$press6t4,n,T)
dew6t4 <- matrix(data$dew6t4,n,T)
prcp6t4 <- matrix(data$prcp6t4,n,T)
wind6t4 <- matrix(data$wind6t4,n,T)
skycover <- matrix(data$skycover,n,T)
ozone <- matrix(data$ozone,n,T)
co <- matrix(data$co,n,T)
lf_model<-Eup(res ~ temp6t410 +press6t4+dew6t4+prcp6t4+wind6t4+skycover+ozone+co, dim.criterion = "PC3")
summary(lf_model)
plot(summary(lf_model))